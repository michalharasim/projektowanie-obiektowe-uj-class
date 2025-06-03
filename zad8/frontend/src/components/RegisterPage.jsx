import AuthForm from "../components/AuthForm";

const RegisterPage = () => {
  const handleRegisterSuccess = () => {
    alert("Registration successful!");
  };

  return (
    <div>
      <h1>Register</h1>
      <AuthForm type="register" onSuccess={handleRegisterSuccess} />
    </div>
  );
};

export default RegisterPage;