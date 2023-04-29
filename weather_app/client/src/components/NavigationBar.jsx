import * as React from 'react';
import {useState} from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import AdbIcon from '@mui/icons-material/Adb';
import {Link } from 'react-router-dom';
import { styled, alpha } from '@mui/material/styles';
import InputBase from '@mui/material/InputBase';
import SearchIcon from '@mui/icons-material/Search';
import Container from '@mui/material/Container';


export default function NavigationBar(props) {
    const [searchValue, setSearchValue] = useState("")


    const handleSubmit = (e) => {
      e.preventDefault();
      console.log(searchValue)
      props.onSearch(searchValue);
    }

    //Material UI styling for Search Bar
const Search = styled('div')(({ theme }) => ({
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing(1),
      width: '20%',
    },
  }));
  //Material UI styling for Search Bar
  const SearchIconWrapper = styled('div')(({ theme }) => ({
    padding: theme.spacing(0, 2),
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  }));
  //Material UI styling for Search Bar
  const StyledInputBase = styled(InputBase)(({ theme }) => ({
    color: 'inherit',
    '& .MuiInputBase-input': {
      padding: theme.spacing(1, 1, 1, 0),
      // vertical padding + font size from searchIcon
      paddingLeft: `calc(1em + ${theme.spacing(4)})`,
      transition: theme.transitions.create('width'),
      width: '100%',
    },
  }));
  


  return (
    //Header Bar
        <>
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
    {/* Search Bar */}
        <Box sx={{ flexGrow: 1}}>
            <AppBar position="static">
                <Toolbar sx={{justifyContent: "center" }}>
                    {/* <Search> 
                    <SearchIconWrapper>
                        <SearchIcon />
                    </SearchIconWrapper>
                    <StyledInputBase placeholder="Search City or Zip" inputProps={{ 'aria-label': 'search'}} type='text'/>
                    </Search> */}
                    <form onSubmit={ handleSubmit }>
                      <input type="text" onChange={(e) => {setSearchValue(e.target.value) }} />
                    </form>
                </Toolbar>
            </AppBar>
        </Box>
    {/* Navigation Bar */}
    <AppBar position="static">
        <Container maxWidth="xl">
            <Toolbar disableGutters>
            <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'flex' }, justifyContent: "center" }}>
                {/* onClick={sendInquiry} */}
                <Button sx={{ my: 2, color: 'white', display: 'block' }}>Today</Button>
                <Button sx={{ my: 2, color: 'white', display: 'block' }}>Hourly</Button>
                <Button sx={{ my: 2, color: 'white', display: 'block' }}>10-Day</Button>
                <Button sx={{ my: 2, color: 'white', display: 'block' }}>Weekend</Button>
            </Box>
            </Toolbar>
        </Container>
    </AppBar>
    </>
  );
}