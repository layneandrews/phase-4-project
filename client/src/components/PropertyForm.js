import { useState } from "react";

const PropertyForm = ({postProperty}) => {
    const [formData, setFormData] = useState({
        address: "",
        city: "",
        state: "",
        image: "",
        bedrooms: 0,
        bathrooms: 0,
        floors: 0
    })

    const handleSubmit = (e) => {
        e.preventDefault()
        postProperty(formData)
        
    }

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    return (
        <div>
            <h1>List a property for sale</h1>
            <form onSubmit={handleSubmit}>
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
               
                <input type="submit" value="List Property"></input>
            </form>
        </div>
    )
}

export default PropertyForm