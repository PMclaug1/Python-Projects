import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';


function ResponsiveAppBar() {

  return (
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
  );
}
export default ResponsiveAppBar;