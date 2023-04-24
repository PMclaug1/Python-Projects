import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import AdbIcon from '@mui/icons-material/Adb';
import {Link } from 'react-router-dom';

export default function ButtonAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
        <AdbIcon/>
          <Typography variant="h6" noWrap component="a" href="/"
          sx={{mr: 2,fontFamily: 'monospace',fontWeight: 700, letterSpacing: '.3rem', color: 'inherit', textDecoration: 'none',}}>
            LOGO
          </Typography>
          <Typography variant="h5" component="div" sx={{ flexGrow: 1, marginRight:6 }}>
            WeatherAPI
          </Typography>
          <Button color="inherit"><Link to={"/login"}>Login</Link></Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}