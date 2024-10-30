import React, { useState } from 'react';
import { Button, TextField, Typography } from '@mui/material';

function UploadFile({ serviceType }) {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = () => {
    if (!file) return;

    // Mock classification response
    const mockGenres = ['Rock', 'Jazz', 'Hip Hop', 'Classical', 'Pop'];
    const randomGenre = mockGenres[Math.floor(Math.random() * mockGenres.length)];

    setResult(`Genre classified by ${serviceType}: ${randomGenre}`);
  };

  return (
    <div style={{ marginTop: 20 }}>
      <TextField
        type="file"
        accept=".wav"
        onChange={handleFileChange}
        fullWidth
        InputLabelProps={{ shrink: true }}
        style={{ marginBottom: 10 }}
      />
      <Button
        variant="contained"
        color="primary"
        onClick={handleSubmit}
        disabled={!file} // Disable button if no file is selected
      >
        Classify Genre
      </Button>
      {result && (
        <Typography variant="body1" style={{ marginTop: 10 }}>
          {result}
        </Typography>
      )}
    </div>
  );
}

export default UploadFile;