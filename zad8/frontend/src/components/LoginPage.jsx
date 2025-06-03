import AuthForm from "../components/AuthForm";

const LoginPage = () => {
  const handleLoginSuccess = () => {
    alert("Login successful!");
  };

  return (
    <div>
      <h1>Login</h1>
      <AuthForm type="login" onSuccess={handleLoginSuccess} />
    </div>
  );
};

export default LoginPage;