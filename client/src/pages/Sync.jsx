import styled from 'styled-components'
import { Button } from '@radix-ui/themes';
import Google from '../graphics/google.svg'
import Microsoft from '../graphics/microsoft.svg'
import Apple from '../graphics/apple.svg'
import Calendar from '../graphics/calendar.svg'
import CalSym from '../graphics/calsym.svg'

function Sync() {
  return (
    <Wrapper>
        <Header>
            <FormTitle>Sync your Calendar</FormTitle>
            <FormSubtitle>Connect your preferred calendar to TimeTogether</FormSubtitle>
        </Header>
        <Wrap>
            <MyCalendar src={Calendar}/>
        </Wrap>
        
        <SyncList>
            <StyledButton type="button" color="gray" variant="solid" highContrast>
                <Graphic src={Google}/>
                Sync with Google
            </StyledButton>
            <StyledButton type="button" color="gray" variant="solid" highContrast>
                <Graphic src={Microsoft}/>
                Sync with Microsoft
            </StyledButton>
            <MyLink as="label" htmlFor="fileUpload" color="gray" variant="solid" highContrast>
                <Wow><Graphic src={CalSym}/> </Wow>
                <span> </span><span>Upload a .ics file</span>
            </MyLink>
            <FileInput type="file" id="fileUpload" accept=".ics"  />
        </SyncList>
    </Wrapper>
  )
}

export default Sync

const Wrapper = styled.div`
  padding: 1em 1em 1.5em 1.5em;
  padding-right:1em;

`

const Header = styled.div`
    margin-bottom:2em;
`

const FormTitle = styled.div`
  font-weight:700;
  font-size:32px;
`

const FormSubtitle = styled.div`
  font-size:14px;
  color:#64748B;
`

const SyncList = styled.div`
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:0.7em;
`

const StyledButton = styled(Button)`
  display:flex;
  width:80%;
  padding: 1.5em;
  background-color:#6C63FF;
  border-radius:8em;
`

const Graphic = styled.img`
    width:15px;
    height:15px;
    margin-right:2px;
`

const MyCalendar = styled.img`
    width:200px;
    align-self:center;
    justify-content:center;
`

const Wrap = styled.div`
    display:flex;
    justify-content:center;
    margin-bottom:3em;
`
const FileInput = styled.input`
  display: none;
`;

const MyLink = styled.div`
display:flex;
justify-content:center;
align-items:center;
    font-weight:500;
    font-size:14px;
    color:white;
    background-color:#6C63FF;
    border-radius: 8em;


    width:80%;
    padding:0.8em;
`

const Wow = styled.div`
    margin-right:5px;
`