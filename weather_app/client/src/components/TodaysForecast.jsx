import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { Container } from '@mui/material'

const bull = (
    <Box
      component="span"
      sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
      •
    </Box>
  );


const TodaysForecast = () => {
  return (
    <div>
    <h1>Today's Weather in Chicago, Illinois</h1>
    <Container sx={{marginY: 5, display: 'flex', justifyContent: 'center'}}>
        {/* Current Date/Time */}
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

        {/* Current Temperature */}
        <Card sx={{ width: '30%', height: '300px'}}>
            <CardContent sx={{marginTop:'50px'}}>
                {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                Word of the Day
                </Typography> */}
                <Typography variant="p" component="div">
                Temperature 
                </Typography>
                <Typography variant="h3" component="div">
                60° 
                </Typography>
                <Typography variant="p" component="div" sx={{marginTop:'20px'}}>
                Feels Like 
                </Typography>
                <Typography variant="h3" component="div">
                53° 
                </Typography>
            </CardContent>
        </Card>
        {/* Current Condition */}
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
        </Card>
    </Container>

    </div>
  )
}

export default TodaysForecast