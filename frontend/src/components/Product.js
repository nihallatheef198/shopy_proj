import React from "react";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";

function Product({ product }) {
  return (
    <Card className="my-3 p-2 rounded ">
      <Link to={`/product/${product._id}`}>
        <Card.Img src={product.image} />
      </Link>
      <Card.Body>
        <Card.Title as="div">
          <strong>{product.name}</strong>
        </Card.Title>
      </Card.Body>

      <Card.Text>
        <Rating value={product.rating} text={`${product.num_reviews} reviews`} color={'#f8e825'} />
      </Card.Text>

      <Card.Text as="h3">
        ${product.price}
      </Card.Text>

    </Card>
  );
}

export default Product;
