// import React, { useState } from 'react';
// import { useNavigate } from 'react-router-dom';


// const Authenticate = ({setUser}) => {
//   const [signUp, setSignUp] = useState(true);
//   const [username, setUsername] = useState('');
//   const [email, setEmail] = useState('');

//   const handleClick = () => setSignUp((signUp) => !signUp)

//   const handleAuth = (e) => {
//     e.preventDefault
//   }

//   return (
//     <>
//         <h2 style={{color: "red"}}>{"Errors Here!!"}</h2>
//         <h2>Please log in or sign up!</h2>
//         <h2>{signUp ? "Current User?": "Not a member?"}</h2>
//         <button onClick={handleClick}>
//             {signUp}
//     </>
//   )

// //   const handleSignUp = async () => {
// //     try {
// //       // Implement sign-up logic here using fetch or any other API library
// //       const response = await fetch('/api/signup', {
// //         method: 'POST',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify({ email, password }),
// //       });

// //       if (response.ok) {
// //         // Handle successful sign-up
// //       } else {
// //         setError('Failed to sign up. Please try again.');
// //       }
// //     } catch (error) {
// //       setError('An error occurred. Please try again.');
// //     }
// //   };

// //   const handleLogin = async () => {
// //     try {
// //       // Implement log-in logic here using fetch or any other API library
// //       const response = await fetch('/api/login', {
// //         method: 'POST',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify({ email, password }),
// //       });

// //       if (response.ok) {
// //         // Handle successful login
// //       } else {
// //         setError('Failed to log in. Please try again.');
// //       }
// //     } catch (error) {
// //       setError('An error occurred. Please try again.');
// //     }
// //   };

// //   return (
// //     <div>
// //       <h2>Sign Up</h2>
// //       <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
// //       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
// //       <button onClick={handleSignUp}>Sign Up</button>

// //       <h2>Log In</h2>
// //       <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
// //       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
// //       <button onClick={handleLogin}>Log In</button>

// //       {error && <p style={{ color: 'red' }}>{error}</p>}

// //       <p>
// //         Already have an account? <Link to="/login">Log in here</Link>.
// //       </p>
// //     </div>
// //   );
// // };

// export default Authenticate;