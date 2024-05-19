import styled from 'styled-components'
import * as Label from '@radix-ui/react-label';
import { Box, TextField } from '@radix-ui/themes';

import {useState, useEffect} from 'react'
function Creds({firstName, lastName, password, updateFields}) {
  const [localFirstName, setLocalFirstName] = useState(firstName);
  const [localLastName, setLocalLastName] = useState(lastName);
  const [localPassword, setLocalPassword] = useState(password);

  useEffect(() => {
    setLocalFirstName(firstName);
    setLocalLastName(lastName);
    setLocalPassword(password);
  }, [firstName, lastName, password]);

  const handleBlur = () => {
    updateFields({
      firstName: localFirstName,
      lastName: localLastName,
      password: localPassword,
    });
  };

  return (
    <Wrapper>
      <Header>
        <FormTitle>What's your name?</FormTitle>
        <FormSubtitle>Provide your account information to begin</FormSubtitle>
      </Header>
      <SubForm>
        <Field>
          <Label.Root className="LabelRoot" htmlFor="firstName">
              First Name
          </Label.Root>
          <TextField.Root id="firstName" radius="full" className="TextFieldRoot" size="3" placeholder="First Name" value={localFirstName}
              onChange={(e) => setLocalFirstName(e.target.value)}
              onBlur={handleBlur}/>
        </Field>
        <Field>
          <Label.Root className="LabelRoot" htmlFor="lastName">
              Last Name
          </Label.Root>
          <TextField.Root id="lastName" radius="full" className="TextFieldRoot" size="3" placeholder="Last Name" value={localLastName}
              onChange={(e) => setLocalLastName(e.target.value)}
              onBlur={handleBlur}/>
        </Field>
        <Field>
          <Label.Root className="LabelRoot" htmlFor="password">
              Password
          </Label.Root>
          <TextField.Root type="password" id="password" radius="full" className="TextFieldRoot" size="3" placeholder="***********" value={localPassword}
              onChange={(e) => setLocalPassword(e.target.value)}
              onBlur={handleBlur}/>
        </Field>
        <Field>
          <Label.Root className="LabelRoot" htmlFor="confirmpass">
              Confirm Password
          </Label.Root>
          <TextField.Root type="password" id="confirmpass" radius="full" className="TextFieldRoot" size="3" placeholder="***********" 
              />
        </Field>
      </SubForm>
    </Wrapper>
  )
}

export default Creds

const Wrapper = styled.div`
  padding: 1em 1em 1em 1em;
  padding-right:1em;
`

const Header = styled.div`

`

const FormTitle = styled.div`
  font-weight:700;
  font-size:32px;
`

const FormSubtitle = styled.div`
  font-size:14px;
  color:#64748B;
`

const SubForm = styled.div`
  margin-top: 1em;
  display:flex;
  flex-direction:column;
  gap:0.5em;

  .LabelRoot {
    font-size:14px;
    padding-left:0.4em;
  }

`

const Field = styled.div`
  
`