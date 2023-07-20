import React from 'react';
import styles from './client/src/index.css'

const Home = () => {
  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <nav>
          {/* Navigation bar with Zillow logo and links */}
        </nav>
      </header>
      <main style={styles.main}>
        {/* Main content */}
        <section style={styles.hero}>
          {/* section with a search bar and call-to-action */}
        </section>
        <section style={styles.featuredProperties}>
          {/* Featured properties */}
          <h2 style={styles.sectionTitle}>Featured Properties</h2>
          <div style={styles.propertyList}>
            {/* Display a list of featured properties */}
          </div>
        </section>
        <section style={styles.searchSection}>
          {/* Additional search options */}
          <h2 style={styles.sectionTitle}>Find Your Dream Home</h2>
          {/* Add search filters and options here */}
        </section>
      </main>
      <footer style={styles.footer}>
        {/* Footer content with links and copyright */}
      </footer>
    </div>
  );
};

export default Home;

// const styles = {
//   container: {
//     fontFamily: 'Arial, sans-serif',
//   },
//   header: {
//     backgroundColor: '#005ba1',
//     color: 'white',
//     padding: '10px',
//   },
//   main: {
//     padding: '20px',
//   },
//   hero: {
//     backgroundColor: '#f0f0f0',
//     padding: '30px',
//     display: 'flex',
//     alignItems: 'center',
//   },
//   sectionTitle: {
//     fontSize: '24px',
//   },
//   featuredProperties: {
//     marginTop: '30px',
//   },
//   propertyList: {
//     display: 'grid',
//     gridTemplateColumns: 'repeat(3, 1fr)',
//     gap: '20px',
//   },
//   searchSection: {
//     marginTop: '30px',
//   },
//   footer: {
//     // Add footer styles here
//   },
// };
