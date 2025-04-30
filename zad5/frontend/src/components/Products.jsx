import React, { useEffect } from "react";
import axios from "axios";
import { useShop } from "./ShopContext";
import { Button, Box, Text, Spinner, Flex, CloseButton, VStack } from "@chakra-ui/react";
import { Table } from "@chakra-ui/react";
import { LuShoppingCart } from "react-icons/lu";
import { Separator } from "@chakra-ui/react";



const Products = () => {
  const { products, setProducts, addToCart, cart, removeFromCart, clearCart } = useShop();

  const sum = cart.reduce((s, p) => s + p.price, 0);

  useEffect(() => {
    axios
      .get("http://localhost:1323/products")
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error("Błąd podczas pobierania produktów:", error);
      });
  }, [setProducts]);
  
  const handlePayment = async () => {
    try {
      await axios.post("http://localhost:1323/payment", {
        cart: { products: cart },
        totalPrice: sum,
      });
  
      clearCart();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Box
      bg="orange.50"
      p={10}
      display="flex"
      flexDirection="column"
      alignItems="center"
      minH="100vh"
    >
      <Box
        bg="white"
        p={6}
        borderRadius="xl"
        boxShadow="lg"
        width="80%"
        maxW="1200px"
        mb={10}
      >
        <Text fontSize="2xl" mb={4} fontWeight="bold" color="orange.600">
          Our Products
        </Text>
        {products.length === 0 ? (
          <Spinner size="xl" color="orange.400" />
        ) : (
          <Table.Root
            size="sm"
            alignSelf="center"
            justifyContent="center"
            interactive
            variant="striped"
            colorScheme="orange"
            maxW="100%"
          >
            <Table.Header background="orange.100">
              <Table.Row>
                <Table.ColumnHeader fontWeight={900} color="orange.700">
                  Product
                </Table.ColumnHeader>
                <Table.ColumnHeader textAlign="end" fontWeight={900} color="orange.700">
                  Price
                </Table.ColumnHeader>
                <Table.ColumnHeader textAlign="end"></Table.ColumnHeader>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {products.map((item) => (
                <Table.Row key={item.id} _hover={{ bg: "orange.50" }}>
                  <Table.Cell>{item.name}</Table.Cell>
                  <Table.Cell textAlign="end">{item.price} zł</Table.Cell>
                  <Table.Cell textAlign="end">
                    <Button
                      onClick={() => addToCart(item)}
                      size="sm"
                      bg="orange.400"
                      color="white"
                      _hover={{ bg: "orange.600" }}
                    >
                      Add to Cart
                    </Button>
                  </Table.Cell>
                </Table.Row>
              ))}
            </Table.Body>
          </Table.Root>
        )}
      </Box>

      <Box
        bg="white"
        p={6}
        borderRadius="xl"
        boxShadow="lg"
        width="80%"
        maxW="1200px"
      >
        <Text fontSize="2xl" mb={4} fontWeight="bold" color="orange.600">
          Your Cart
        </Text>
        {cart.length === 0 ? (
          <Flex direction="column" align="center" justify="center" color="gray.500">
            <Box fontSize="4xl" mb={2}>
              <LuShoppingCart />
            </Box>
            <Text fontWeight="bold">Your cart is empty</Text>
          </Flex>
        ) : (
          <VStack spacing={4} align="stretch">
            {cart.map((p, i) => (
              <Box key={i}>
                <Flex justify="space-between" align="center">
                  <Text>
                    {p.name} - {p.price} zł
                  </Text>
                  <CloseButton
                    onClick={() => removeFromCart(i)}
                    size="sm"
                    color="red.500"
                    _hover={{ bg: "red.600" }}
                  />
                </Flex>
                <Separator mt={2} mb={2} />
              </Box>
            ))}
            <Text fontWeight="bold">Sum: {sum} zł</Text>
            <Button
              backgroundColor="orange.400"
              color="white"
              size="md"
              _hover={{ bg: "orange.600" }}
              onClick={handlePayment}
            >
              Buy
            </Button>
          </VStack>
        )}
      </Box>
    </Box>
  );
};

export default Products;