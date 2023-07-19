import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './home';
import PropertyList from './propertyList';
import PropertyDetails from './propertyDetails';
import ReviewForm from './reviews';

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/properties" element={<PropertyList />} />
        <Route path="/property/:id" element={<PropertyDetails />} />
        <Route path="/review" element={<ReviewForm />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
