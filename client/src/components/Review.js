import React from 'react';

const ReviewForm = () => {
  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission goes here!
  };

  return (
    <div>
      <h1>Leave a Review</h1>
      <form onSubmit={handleSubmit}>
        {/* Add form for leaving a review! */}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default ReviewForm;
