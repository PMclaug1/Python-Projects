import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

const bull = (
  <Box
    component="span"
    sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
  >
    •
  </Box>
);

export default function CurrentDateTime() {
  return (
    <Card sx={{ width: '30%', height: '300px'}}>
      <CardContent sx={{alignItems: 'center', justifyContent:'center', marginTop:'100px'}}>
        <Typography variant="h5" component="div">
          April 21st, 2023
        </Typography>
        <Typography variant="h5" component="div">
          1:07 PM
        </Typography>
      </CardContent>
    </Card>
  );
}