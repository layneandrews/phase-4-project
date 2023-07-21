import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const PropertyDetail = () => {
  const [propertyDetail, setPropertyDetail] = useState({})
  const {id} = useParams()
  useEffect(() => {
    fetch(`http://127.0.0.1:5555/properties/${id}`) 
    .then(res => res.json())
    .then((oneProp) => {
      console.log(oneProp)
      setPropertyDetail(oneProp)
    })
  },[])

  return (
    <div>
      <img src={propertyDetail.image}/>
      <h1>{propertyDetail.address}</h1>
      <h3>{propertyDetail.city}</h3>
      <h3>{propertyDetail.state}</h3>
      <h3>Bedrooms: {propertyDetail.bedrooms}</h3>
      <h3>Bathrooms: {propertyDetail.bathrooms}</h3>
      <h3>Floors: {propertyDetail.floors}</h3>
      
    </div>
  );
};

export default PropertyDetail;

