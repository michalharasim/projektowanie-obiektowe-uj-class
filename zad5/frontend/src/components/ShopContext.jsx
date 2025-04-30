import React, { createContext, useContext, useState, useEffect } from "react";

const ShopContext = createContext();

export const useShop = () => useContext(ShopContext);

export const ShopProvider = ({ children }) => {
  const [products, setProducts] = useState([]);

  const [cart, setCart] = useState(() => {
    const storedCart= localStorage.getItem("cart");
    return storedCart ? JSON.parse(storedCart) : [];
  });

  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));
  }, [cart]);

  const addToCart = (produkt) => {
    setCart([...cart, produkt]);
  };

  const removeFromCart = (index) => {
    setCart((prevCart) => prevCart.filter((_, i) => i !== index));
  };

  const clearCart = () => setCart([]);

  return (
    <ShopContext.Provider
      value={{
        products,
        setProducts,
        cart,
        addToCart,
        clearCart,
        removeFromCart,
      }}
    >
      {children}
    </ShopContext.Provider>
  );
};