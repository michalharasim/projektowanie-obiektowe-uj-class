import { useState } from "react";
import axios from "axios";
import {
  Button,
  Box,
  Input,
  Flex,
  Text
} from "@chakra-ui/react";
import {
  FormControl,
  FormErrorMessage,
  FormLabel,
} from "@chakra-ui/form-control";
import { useNavigate } from "react-router-dom";

const AuthForm = ({ type, onSuccess }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      setError("");
  
      try {
        const url = type === "login" ? "/login" : "/register";
        const response = await axios.post(`http://localhost:1323${url}`, {
          username,
          password,
        });
  
        if (response.data.token) {
          localStorage.setItem("token", response.data.token);
          onSuccess();
          if (type === "login") {
            navigate("/protected");
          }
        } else {
          if (type === "register") {
            alert("Registration successful! Please log in.");
            navigate("/login");
          } else {
            alert(`${type} successful!`);
          }
        }
      } catch (err) {
        setError("An error occurred. Please try again.");
        alert("An error occurred. Please try again.");
      }
    };
  
    return (
      <Flex justify="center" align="center" height="100vh">
        <Box bg="gray.50" p={6} borderRadius="xl" boxShadow="lg" width="300px">
          <FormControl isInvalid={error}>
            <FormLabel>Username</FormLabel>
            <Input
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Username"
              required
            />
          </FormControl>
          <FormControl isInvalid={error} mt={4}>
            <FormLabel>Password</FormLabel>
            <Input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              type="password"
              placeholder="Password"
              required
            />
          </FormControl>
          {error && <FormErrorMessage>{error}</FormErrorMessage>}
          <Button mt={4} colorScheme="orange" onClick={handleSubmit}>
            {type === "login" ? "Login" : "Register"}
          </Button>
          {type === "login" && (
            <Text mt={2}>
              Don't have an account?{" "}
              <Text
                as="span"
                color="blue.500"
                cursor="pointer"
                onClick={() => navigate("/register")}
              >
                Register here
              </Text>
            </Text>
          )}
          {type === "register" && (
            <Text mt={2}>
              Already have an account?{" "}
              <Text
                as="span"
                color="blue.500"
                cursor="pointer"
                onClick={() => navigate("/login")}
              >
                Login here
              </Text>
            </Text>
          )}
          {type === "login" && (
            <Button
              mt={4}
              colorScheme="teal"
              onClick={() => navigate("/protected")}
              width="100%"
            >
              Go to Protected Page
            </Button>
          )}
        </Box>
      </Flex>
    );
  };
  
  export default AuthForm;