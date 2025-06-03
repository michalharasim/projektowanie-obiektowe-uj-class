import { Routes, Route } from "react-router-dom";
import RegisterPage from "./components/RegisterPage";
import LoginPage from "./components/LoginPage";
import ProtectedPage from "./components/ProtectedPage";

function App() {
  return (
    <>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage/>} />
        <Route path="/protected" element={<ProtectedPage />} />
      </Routes>
    </>
  );
}

export default App;