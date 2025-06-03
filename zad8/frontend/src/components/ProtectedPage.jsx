import { useEffect, useState } from "react";
import axios from "axios";
import { Box, Text, Flex, Button } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

const ProtectedPage = () => {
    const [message, setMessage] = useState("");
    const [status, setStatus] = useState("info");
    const navigate = useNavigate();
  
    useEffect(() => {
      const token = localStorage.getItem("token");
  
      if (!token) {
        setMessage("You are not authenticated.");
        setStatus("error");
        return;
      }
  
      axios
        .get("http://localhost:1323/protected", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })
        .then((response) => {
          setMessage(response.data.message || "Access granted!");
          setStatus("success");
        })
        .catch((error) => {
          setMessage("Access denied. Please login again.");
          setStatus("error");
        });
    }, []);
  
    return (
      <Flex justify="center" align="center" height="100vh">
        <Box p={6} maxWidth="600px" width="100%" borderRadius="md" boxShadow="lg">
          {status === "error" ? (
            <Box p={4} bg="red.500" color="white" borderRadius="md" boxShadow="md" width="100%">
              <Text fontSize="lg" fontWeight="bold">
                Error:
              </Text>
              <Text>{message}</Text>
            </Box>
          ) : status === "success" ? (
            <Box p={4} bg="green.500" color="white" borderRadius="md" boxShadow="md" width="100%">
              <Text fontSize="lg" fontWeight="bold">
                Success:
              </Text>
              <Text>{message}</Text>
            </Box>
          ) : (
            <Text>Loading...</Text>
          )}
  
          <Button
            mt={4}
            colorScheme="blue"
            onClick={() => navigate("/login")}
            width="100%"
          >
            Go to Login Page
          </Button>
        </Box>
      </Flex>
    );
  };
  
  export default ProtectedPage;