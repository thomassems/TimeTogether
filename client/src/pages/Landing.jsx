import { useState } from 'react'
import styled from 'styled-components'
import Love from '../graphics/fun.svg'

function Landing() {

  return (
    <Main>
      <Header>
        <Title>Time<Color>Together</Color></Title>
        <SubTitle>Never miss a chance with friends.</SubTitle>
        <Graphic src={Love} alt="" />
      </Header>
    </Main>
  )
}

export default Landing

const Main = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box; /* Ensure padding is included in element's width and height */
  overflow-x: hidden; /* Prevent horizontal scrolling */
  overflow-y: hidden;
`

const Color = styled.span`
  color:#6C63FF;
`


const Header = styled.div`
  display:flex;
  flex-direction:column;
  min-height:400px;
  align-items:center;
`

const Title = styled.p`
  font-size:3em;
  font-weight:700;
  padding:0;
  padding-top:1em;
`

const SubTitle = styled.p`
  color:#64748B;
  margin-bottom:2em;
`

const Graphic = styled.img`
  width:300px;
`
