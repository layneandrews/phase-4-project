import { useState } from "react";
import { useParams } from "react-router-dom";

const PropertyEditForm = ({patchProperty, editProperty}) => {
    const [formData, setFormData] = useState({...editProperty})

    const handleEditSubmit = (e) => {
        e.preventDefault()
        console.log(formData)
        patchProperty({
            image: formData.image,
            address: formData.address,
            city: formData.city,
            state: formData.state,
            bedrooms: formData.bedrooms,
            bathrooms: formData.bathrooms,
            floors: formData.floors
        },
        editProperty.id
        )
    }

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    return (
        <div>
            <h1>Edit property details</h1>
            <form onSubmit={handleEditSubmit}>
                <label>
                    Image:
                    <input name="image" value={formData.image} onChange={handleChange}/>
                </label>
                <label>
                    Address:
                    <input name="address" value={formData.address} onChange={handleChange}/>
                </label>
                <label>
                    City:
                    <input name="city" value={formData.city} onChange={handleChange}/>
                </label>
                <label>
                    State:
                    <input name="state" value={formData.state} onChange={handleChange}/>
                </label>
                
                <label>
                    Bedrooms:
                    <input name="bedrooms" value={formData.bedrooms} onChange={handleChange}/>
                </label>
                <label>
                    Bathrooms:
                    <input name="bathrooms" value={formData.bathrooms} onChange={handleChange}/>
                </label>
                <label>
                    Floors:
                    <input name="floors" value={formData.floors} onChange={handleChange}/>
                </label>
               
                <input type="submit" value="Update Property"></input>
            </form>
        </div>
    )
}

export default PropertyEditForm