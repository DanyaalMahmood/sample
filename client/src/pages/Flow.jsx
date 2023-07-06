import React from 'react';
import ReactFlow, {
    MiniMap,
    Controls,
    Background,
    MarkerType
  } from 'reactflow';
import { useState, useEffect } from 'react';
import axios from 'axios';
import 'reactflow/dist/style.css';

function Flow() {

    const [data, setData] = useState([]);

    const getData = async () => {
        const response = await axios.get("http://127.0.0.1:105/flow");
        await setData(response.data);
        console.log('Response Data:', response.data);
    }
    useEffect(() => {
        console.log('component mounted')
        getData();
    }, []);

    return(
        <div style={{ width: '100vw', height: '100vh' }}>
            <ReactFlow nodes={data.initialNodes} edges={data.initialEdges} >
                <Controls />
                <MiniMap />
                <Background variant="dots" gap={12} size={1} />
            </ReactFlow>
        </div>
    )
}

export default Flow;