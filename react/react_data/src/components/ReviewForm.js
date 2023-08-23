import { useState } from "react";

function ReviewForm() {
  const [title, setTitle] = useState("");
  const [rating, setRating] = useState(0);
  const [content, setContent] = useState("");

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleRatingChange = (e) => {
    const nextRating = Number(e.taget.value) || 0;
    setRating(nextRating);
  };

  const handleContentChange = (e) => {
    setContent(e.target.value);
  };

  const handleSubmit = () => {
    console.log({
      title,
      rating,
      content,
    });
  };

  return (
    <form className="ReviewForm" onSubmit={handleSubmit}>
      <input value={title} onChange={handleTitleChange} />
      <input type="number" value={rating} onChange={handleRatingChange} />
      <textarea value={content} onChange={handleContentChange} />
      <button type="submit">확인</button>
    </form>
  );
}

export default ReviewForm;