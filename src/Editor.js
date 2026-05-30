import React, { useEffect, useRef, useState } from "react";

import axios from "axios";
import debounce from "lodash.debounce";

import ReactQuill from "react-quill-new";
import "quill/dist/quill.snow.css";

function Editor() {
  const docId = 1;

  const [value, setValue] = useState("");

  const socketRef = useRef(null);

  useEffect(() => {

    // Load initial document
    axios
      .get(`http://127.0.0.1:8000/api/document/${docId}/`)
      .then((res) => {
        setValue(res.data.content);
      });

    // WebSocket
    socketRef.current = new WebSocket(`ws://127.0.0.1:8000/ws/editor/${docId}/`);

    socketRef.current.onmessage = (event) => {
      const data = JSON.parse(event.data);

      setValue(data.content);
    };

    return () => {
      socketRef.current.close();
    };

  }, []);

  const sendChanges = debounce((content) => {
    socketRef.current.send(
      JSON.stringify({
        content,
      })
    );
  }, 300);

  const handleChange = (content) => {
    setValue(content);
    sendChanges(content);
  };

  return (
    <div style={{ width: "100vh", margin: "150px auto" , height: "50vh", overflow: "scroll", backgroundColor: "white"
    , color: "black", fontSize: "20px", padding: "20px", border: "1px solid black", borderRadius: "10px"
    }}>
      <ReactQuill value={value} onChange={handleChange} />
    </div>
  );
}

export default Editor;