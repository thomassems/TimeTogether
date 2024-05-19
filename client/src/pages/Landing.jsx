import { useState } from 'react'
import styled from 'styled-components'
import Love from '../graphics/love.svg'

function Landing() {

  return (
    <Main>
      <Header>
        <Title>TimeTogether</Title>
        <SubTitle>Never miss a moment with friends.</SubTitle>
        <Graphic src={Love} alt="" />
      </Header>
    </Main>
  )
}

export default Landing

const Main = styled.div`
  margin: 1em 1em 1em 1em;
  padding: 1em;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box; /* Ensure padding is included in element's width and height */
  overflow-x: hidden; /* Prevent horizontal scrolling */
  overflow-y: hidden;
`


const Header = styled.div`
  display:flex;
  flex-direction:column;
  min-height:400px;
  justify-content:center;
  align-items:center;
`

const Title = styled.p`
  font-size:3em;
  font-weight:700;
  margin-bottom:-0.2em;
  padding:0;
`

const SubTitle = styled.p`
  color:#64748B;
`

const Graphic = styled.img`
  margin-top:2em;
  width:250px;
`
