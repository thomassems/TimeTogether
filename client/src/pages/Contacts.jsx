import styled from "styled-components";
import * as Avatar from "@radix-ui/react-avatar";
import { Button, Select } from "@radix-ui/themes";
import { useState } from "react";

const users = [
  {
    name: "Thomas Semczyszyn",
    location: "From your contacts",
    img: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4VOhplf0DCBkYcC-2_QQIgTZJOouukqRVFa4plFS3yg&s"
  },
  {
    name: "Evan Yan",
    location: "From your contacts",
    img: 'https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/0/a/1/0a1dcd77e33d49eb5b23b682629c7fcc39d4f39f.jpeg'
  },
  {
    name: "Solemann Mateen",
    location:"From your contacts",
    img: 'https://i.pinimg.com/564x/a7/5d/62/a75d62adddc8397c7820df76d8d05a30.jpg'
  }, 
  {
    name: "Nick Pestov",
    location: "From your contacts",
    img: 'https://static.planetminecraft.com/files/image/minecraft/blog/2020/264/13717841-steveheadiconx_l.jpg'
  }
];

function Contacts() {
    const [pending, setPending] = useState(Array(users.length).fill(false));

    const handleButtonClick = (index) => {
      setPending((prev) => {
        const newPending = [...prev];
        newPending[index] = true;
        return newPending;
      });
    };
    
  return (
    <Wrapper>
      <Header>
        <FormTitle>Add your Contacts</FormTitle>
        <FormSubtitle>Send friend requests to your contacts</FormSubtitle>
        <List>
          {users.map(({ name, location, img }, i) => (
            <User id={i}>
              <Avatar.Root className="AvatarRoot">
                <Avatar.Image
                  className="AvatarImage"
                  src={img}
                  alt="Colm Tuite"
                />
                <Avatar.Fallback className="AvatarFallback" delayMs={600}>
                  null
                </Avatar.Fallback>
              </Avatar.Root>
              <Text>
                <UserTitle>{name}</UserTitle>
                <UserLoc>{location}</UserLoc>
                <Buttons>

                  <Select.Root defaultValue="low">
                    <StyledSelectTrigger variant="surface" radius="full" />
                    <Select.Content>
                      <Select.Item id="SelectItem" value="high">High Priority</Select.Item>
                      <Select.Item value="medium">Medium Prority</Select.Item>
                      <Select.Item value="low">Low Priority</Select.Item>
                    </Select.Content>
                  </Select.Root>


                  {pending[i] ? (
                    <PendingButton color="gray" highContrast type="button"><span></span>Pending<span></span></PendingButton>
                  ) : (
                    <StyledButton
                      type="button"
                      color="gray"
                      variant="solid"
                      highContrast
                      onClick={() => handleButtonClick(i)}
                    >
                      Add Friend
                    </StyledButton>
                  )}
                </Buttons>
              </Text>
            </User>
          ))}
        </List>
      </Header>
    </Wrapper>
  );
}

export default Contacts;

const Wrapper = styled.div`
  padding: 1em 1em 1em 1em;
  padding-right: 1em;
`;

const Header = styled.div``;

const FormTitle = styled.div`
  font-weight: 700;
  font-size: 32px;
`;

const FormSubtitle = styled.div`
  font-size: 14px;
  color: #64748b;
`;

const User = styled.div`
  display: flex;
  flex-direction: row;
  .AvatarRoot {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    overflow: hidden;
    user-select: none;
    width: 75px;
    height: 75px;
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
`;

const Text = styled.div`
  display: flex;
  flex-direction: column;
  padding: 0em 1em 1em 1em;
`;

const UserTitle = styled.div`
  font-weight: 500;
  font-size: 16px;
`;

const UserLoc = styled.div`
  font-size: 12px;
  color: #64748b;
`;

const List = styled.div`
  margin-top: 2em;
`;

const Buttons = styled.div`
  padding-top:0.2em;
  display: flex;
  flex-direction: row;
  gap:0.5em;


`;

const StyledSelectTrigger = styled(Select.Trigger)`
width: 120px; /* Fixed width */
padding: 0 1em; /* Adjust padding as needed */
display: flex;
justify-content: space-between; /* Ensure proper alignment of content */
align-items: center; /* Center content vertically */
`;

const StyledButton = styled(Button)`
  display: flex;
  border-radius: 2em;
  padding: 0em 2em;
`;


const PendingButton = styled(Button)`
display: flex;
border-radius: 2em;
padding: 0em 2em;
background-color: white; /* White background to appear hollow */
border: 2px solid #000; /* Black border for the outline */
color: #000; /* Black text color */
cursor: default;

`