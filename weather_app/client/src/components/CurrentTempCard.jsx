import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Homepage from '../views/Homepage';
import weatherData from '../views/Homepage';
import { useState } from '../views/Homepage'

const bull = (
    <Box
        component="span"
        sx={{ display: 'inline-block', mx: '2px', transform: 'scale(0.8)' }}
    >
        •
    </Box>
);


export default function Current_Temp_Card() {
    console.log(weatherData)
    return (
        <Card sx={{ width: '30%', height: '300px' }}>
            <CardContent sx={{ marginTop: '50px' }}>
                {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          Word of the Day
        </Typography> */}
                <Typography variant="p" component="div">
                    Temperature
                </Typography>
                <Typography variant="h3" component="div">
                    {weatherData.temp_f}
                </Typography>
                <Typography variant="p" component="div" sx={{ marginTop: '20px' }}>
                    Feels Like
                </Typography>
                <Typography variant="h3" component="div">
                    53°
                </Typography>
            </CardContent>

        </Card>
    );
}