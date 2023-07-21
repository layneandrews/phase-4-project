import PropertyCard from "./PropertyCard"

const PropertyContainer = ({properties, setEditProperty, deleteProperty}) => {
    const mappedProperties = () => 
        properties.map((prop) => (
            <PropertyCard key={prop.id} property={prop} setEditProperty={setEditProperty} deleteProperty={deleteProperty}/>)
        )

    return <div>{mappedProperties()}</div>
}

export default PropertyContainer


// import React from 'react'
// import styles from '../index.css'


// const PropertyContainer = ({properties}) => {
//     return (
//         <div>
//             <Title>Leaf Stone Properties</Title>
//             <CardContainer>
                
//             </CardContainer>
//         </div>
//     )
// }







// export default PropertyContainer
