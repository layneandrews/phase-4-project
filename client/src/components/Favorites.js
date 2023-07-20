import React, { useState } from 'react';

const Favorites = () => {
  const [favorites, setFavorites] = useState([]);

  // demo property data 
  const properties = [
    { id: 1, name: 'Beautiful House' },
    { id: 2, name: 'Cozy Apartment' },
    { id: 3, name: 'Luxury Villa' },
    // Add more properties
  ];

  const handleAddToFavorites = (property) => {
    setFavorites((prevFavorites) => [...prevFavorites, property]);
  };

  const handleRemoveFromFavorites = (propertyId) => {
    setFavorites((prevFavorites) =>
      prevFavorites.filter((property) => property.id !== propertyId)
    );
  };

  return (
    <div>
      <h1>My Favorites</h1>
      <div>
        {/* Display the list of properties */}
        <ul>
          {properties.map((property) => (
            <li key={property.id}>
              <span>{property.name}</span>
              {favorites.find((favProperty) => favProperty.id === property.id) ? (
                <button onClick={() => handleRemoveFromFavorites(property.id)}>
                  Remove from Favorites
                </button>
              ) : (
                <button onClick={() => handleAddToFavorites(property)}>
                  Add to Favorites
                </button>
              )}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Favorites;
