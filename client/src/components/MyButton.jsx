import { Button } from '@radix-ui/themes';
import styled from 'styled-components'

function MyButton({text}) {
  return (
    <Footer>
    <StyledButton color="gray" variant="solid" highContrast>
      { text }
    </StyledButton>
  </Footer>
  )
}

export default MyButton

const Footer = styled.div`
  position: absolute;
  bottom: 4em; /* Adjust this value to move the button higher or lower */
  width: 100%;
  display: flex;
  justify-content: center;
`;

const StyledButton = styled(Button)`
  display:flex;
  width:95%;
  padding: 1.6em;
`