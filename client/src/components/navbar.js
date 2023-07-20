import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });

  const handleLogin = (event) => {
    event.preventDefault();
    //   add the login info for authentication and using the loginData state.
    console.log('Login data:', loginData);
    // Example: Call a login API with the loginData.
  };

  return (
    <>
      {/* Header */}
      <header style={styles.header}>
        <h1 style={styles.title}>Leaf Stone</h1>
      </header>

      {/* Navbar */}
      <nav style={styles.nav}>
        <ul style={styles.navList}>
          <li style={styles.navItem}>
            <Link to="/">Home</Link>
          </li>
          <li style={styles.navItem}>
            <Link to="/properties">Properties</Link>
          </li>
          <li style={styles.navItem}>
            <Link to="/buy">Buy</Link>
          </li>
          <li style={styles.navItem}>
            <Link to="/sell">Sell</Link>
          </li>
          <li style={styles.navItem}>
            <Link to="/favorites">Favorites</Link>
          </li>
        </ul>
        <div style={styles.loginForm}>
          <form onSubmit={handleLogin}>
            <label>
              Username:
              <input
                type="text"
                name="username"
                value={loginData.username}
                onChange={(e) => setLoginData({ ...loginData, username: e.target.value })}
              />
            </label>
            <label>
              Password:
              <input
                type="password"
                name="password"
                value={loginData.password}
                onChange={(e) => setLoginData({ ...loginData, password: e.target.value })}
              />
            </label>
            <button type="submit">Login</button>
          </form>
        </div>
      </nav>
    </>
  );
};

export default NavBar;

const styles = {
  header: {
    backgroundColor: '#005ba1',
    textAlign: 'center',
    padding: '20px',
    marginBottom: '20px',
    color: 'white',
  },
  title: {
    fontSize: '36px',
    fontWeight: 'bold',
    textTransform: 'uppercase',
  },
  nav: {
    backgroundColor: '#005ba1',
    color: 'blue',
    padding: '10px',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center', 
  },
  navList: {
    listStyle: 'none',
    display: 'flex',
    alignItems: 'center', 
    color: 'green',
  },
  navItem: {
    marginRight: '20px',
  },
  loginForm: {
    display: 'flex',
    alignItems: 'center', 
    color: 'white',
  },
};
