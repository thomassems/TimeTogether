import NavBar from "../components/NavBar"
import { Route, Routes } from 'react-router-dom';
import Home from './Home';
import Friends from './Friends';
import Settings from './Settings';
import * as Avatar from "@radix-ui/react-avatar";
import styled from "styled-components";

function Hub({data}) {
  const {firstName, lastName} = data;
  return (
    <Wrapper>
      <Header>
        <Avatar.Root className="AvatarRoot">
                  <Avatar.Image
                    className="AvatarImage"
                    src='https://sites.uci.edu/sbass/files/2022/05/AF7A55DF-ABEE-4850-B93D-846C75426F32-400x400.png'
                    alt="Colm Tuite"
                  />
                  <Avatar.Fallback className="AvatarFallback" delayMs={600}>
                    null
                  </Avatar.Fallback>
        </Avatar.Root>
        <Text>
          <Morning>Good Morning</Morning>
          <Name>{firstName} {lastName}</Name>
        </Text>
      </Header>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/friends" element={<Friends />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
      <NavBar/>
    </Wrapper>
  )
}

export default Hub

const Wrapper = styled.div`
  margin: 1.5em 1.5em 1.5em 1.5em;
`

const Header = styled.div`
  display:flex;
  flex-direction:row;
  .AvatarRoot {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    overflow: hidden;
    user-select: none;
    width: 50px;
    height: 50px;
    border-radius: 100%;
    background-color: var(--black-a3);
  }

  .AvatarImage {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
  }

  .AvatarFallback {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: white;
    color: var(--violet-11);
    font-size: 15px;
    line-height: 1;
    font-weight: 500;
  }

`

const Text = styled.div`
  display:flex;
  flex-direction:column;
  margin-top:6px;
  margin-left:1em;
  
`

const Morning = styled.div`
  color:#5E5E5E;
  font-size:12px;
  margin-bottom:-5px;
`

const Name = styled.div`
  font-weight:700;
  font-size:16px;
`