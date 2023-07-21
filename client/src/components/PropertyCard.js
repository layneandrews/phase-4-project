import { useNavigate } from "react-router"
const PropertyCard = ({property, setEditProperty, deleteProperty}) => {
    const {address, city, state, image, bedrooms, bathrooms, floors, id} = property
    const nav = useNavigate()

    const handleEditButton = e => {
        setEditProperty(property)
        nav(`/properties/edit/${property.id}`)
    }

    const handleDeleteButton = e => {
        deleteProperty(id)
    }

    return (
        <div>
            <img src={image} onClick={() => nav(`/properties/${id}`)}/>
            <h3>{address}</h3>
            <p>{city}</p>
            <p>{state}</p>
            

            <button onClick={handleEditButton}>Edit</button>
            <button onClick={handleDeleteButton}>Delete</button>
        </div>
    )
}

export default PropertyCard
