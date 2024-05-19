import Landing from './pages/Landing'
import Form from './pages/Form'
import {createGlobalStyle} from "styled-components"
import styled from 'styled-components'
function App() {

  return (
    <>
      <GlobalStyle/>
      <Form/>
    </>
  )
}

export default App

const GlobalStyle = createGlobalStyle`
  body {
    font-family: "Inter", sans-serif;
    max-width:600px;
    margin: auto;
    // margin:auto;
  }

`
