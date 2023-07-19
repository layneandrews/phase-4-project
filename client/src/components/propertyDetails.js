import React from 'react';
import { useParams } from 'react-router-dom';

const PropertyDetails = () => {
  const { id } = useParams();

  return (
    <div>
      <h1>Property Details for Property ID: {id}</h1>
      {/* Add property details here! */}
    </div>
  );
};

export default PropertyDetails;

