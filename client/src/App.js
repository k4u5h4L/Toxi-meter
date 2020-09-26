import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState(0);
  const [submit, setSubmit] = useState(false);

  useEffect(() => {
    const postData = async () => {
      axios
        .post("http://localhost:8000/api/", {
          review: query,
        })
        .then((response) => {
          // console.log(response.data);
          setResult(response.data.message);
        })
        .catch((error) => {
          console.error(error);
        });
    };

    postData();
  }, [submit]);

  const handleChange = (e) => {
    // console.log(`query: ${query}`);
    setQuery(e.target.value);
  };

  const handleSubmit = () => {
    setSubmit(!submit);
  };

  return (
    <div
      className="container-contact100"
      style={{ backgroundImage: "url('images/bg-01.jpg')" }}
    >
      <div className="wrap-contact100">
        <form className="contact100-form validate-form">
          <span className="contact100-form-title">
            Input a movie review to determine whether it's positive or not!
          </span>

          <div
            className="wrap-input100 validate-input"
            data-validate="Message is required"
          >
            <span className="label-input100">Movie Review</span>
            <textarea
              className="input100"
              name="headline"
              placeholder="Enter Review Here..."
              value={query}
              onChange={(event) => handleChange(event)}
            ></textarea>
          </div>

          <div className="wrap-input100">
            <span className="label-input100">Result</span>
            <input
              style={{ color: result ? "green" : "red" }}
              className="input100"
              type="text"
              name="web"
              placeholder="Result"
              readOnly={true}
              value={
                result
                  ? "I think this is a positive review"
                  : "I don't think this is a positive review"
              }
            />
          </div>

          <div className="container-contact100-form-btn">
            <div className="wrap-contact100-form-btn">
              <div className="contact100-form-bgbtn"></div>
              <button
                type="button"
                className="contact100-form-btn"
                onClick={() => handleSubmit()}
              >
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>

      <span className="contact100-more">
        Powered by React, Django and Tensorflow-Keras
      </span>
    </div>
  );
};

export default App;
