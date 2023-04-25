import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function Current_Icon_Condition() {
  return (
    <Card sx={{ width: '30%', height: '300px'}}>
      <CardMedia
        sx={{width: 1/2, height: 1/2, marginLeft: 9, marginTop: 3 }}
        image="https://static.vecteezy.com/system/resources/previews/008/310/370/original/partly-cloudy-i-flat-multicolor-icon-vector.jpg"
        title="weather icon"
      />
      <CardContent>
        <Typography variant="h5">
          Partly Cloudy
        </Typography>
      </CardContent>
      {/* <CardActions>
        <Button size="small">Share</Button>
        <Button size="small">Learn More</Button>
      </CardActions> */}
    </Card>
  );
}