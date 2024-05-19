import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import '@radix-ui/themes/styles.css';
import { BrowserRouter } from 'react-router-dom';
import { Theme } from '@radix-ui/themes';
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Theme>
    <BrowserRouter>
      <App />
      </BrowserRouter>
    </Theme>
  </React.StrictMode>,
)
