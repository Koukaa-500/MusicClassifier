import logo from './logo.svg';
import './App.css';
import UploadFile from './components/UploadFile';
import { Button, Card, CardContent, Typography } from '@mui/material';
function App() {
  return (
    <div className="App">
      <Card style={{ maxWidth: 345, margin: "100px auto" }}>
        <CardContent>
          <Typography variant="h5" component="div">
            Music Genre Classification
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Upload your .wav file to classify its genre using Machine Learning!
          </Typography>
          <UploadFile serviceType="SVM_service" />
          <UploadFile serviceType="vgg19_service" />
        </CardContent>
      </Card>
    </div>
  );
}

export default App;
