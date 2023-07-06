import { useState, useEffect } from "react";
import axios from 'axios';

function Sample() {
    const [data, setData] = useState([]);

    const getData = async () => {
        const response = await axios.get("http://127.0.0.1:105/sample");
        await setData(response.data);
        console.log('Response Data:', response.data);
    }
    useEffect(() => {
        console.log('component mounted')
        getData();
    }, []);


    return (
        <div className="flex flex-col justify-center items-center h-screen">
            <div className="flex m-4 font-bold">
                <h1 className="text-2xl mr-10">Name</h1>
                <p className="text-2xl">Address</p>
            </div>
            {data.map((item) => (
                <div key={item.name} className="flex m-4">
                    <h1 className="text-2xl mr-10">{item.name}</h1>
                    <p className="text-2xl">{item.address}</p>
                </div>
            ))}
        </div>
    )
}

export default Sample;