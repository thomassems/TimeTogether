import styled from "styled-components";
import * as Avatar from "@radix-ui/react-avatar";
import { Button } from "@radix-ui/themes";

function ContactCard({ name, priority, lastHangout, isAvailable, event }) {
  const renderPriorityButton = (priority) => {
    switch (priority) {
      case 1:
        return <HighPriorityButton>High Priority</HighPriorityButton>;
      case 2:
        return <MediumPriorityButton>Medium Priority</MediumPriorityButton>;
      case 3:
        return <LowPriorityButton>Low Priority</LowPriorityButton>;
      default:
        return null;
    }
  };
  return (
    <>
      {isAvailable ? (
        <AvailCard>
          <Profile>
            <Avatar.Root className="AvatarRoot">
              <Avatar.Image
                className="AvatarImage"
                src="https://devforum-uploads.s3.dualstack.us-east-2.amazonaws.com/uploads/original/4X/0/a/1/0a1dcd77e33d49eb5b23b682629c7fcc39d4f39f.jpeg"
                alt="Colm Tuite"
              />
              <Avatar.Fallback className="AvatarFallback" delayMs={600}>
                null
              </Avatar.Fallback>
            </Avatar.Root>
            <Text>
              <Name>{name}</Name>
              {renderPriorityButton(priority)}
            </Text>
          </Profile>
          <Availability>
            <AvailText>
              You both share availability on <br></br>
              <b>{event.date} </b>
              <br></br>
              Accept if you are willing to time together.
            </AvailText>
            <Buttons>
              <StyledButton
                type="button"
                color="gray"
                variant="solid"
                highContrast
              >
                Accept
              </StyledButton>
              <PendingButton
                type="button"
                color="gray"
                variant="solid"
                highContrast
              >
                Decline
              </PendingButton>
            </Buttons>
          </Availability>
        </AvailCard>
      ) : (
        <DefCard>
          <Profile>
            <Avatar.Root className="AvatarRoot">
              <Avatar.Image
                className="AvatarImage"
                src="https://cdn-icons-png.flaticon.com/512/4646/4646084.png"
                alt="Colm Tuite"
              />
              <Avatar.Fallback className="AvatarFallback" delayMs={600}>
                null
              </Avatar.Fallback>
            </Avatar.Root>
            <Text>
              <Name>{name}</Name>
              {renderPriorityButton(priority)}
            </Text>
          </Profile>
          <Availability>
            <AvailText>
              You both don't share any times at the moment.
            </AvailText>
          </Availability>
        </DefCard>
      )}
    </>
  );
}

export default ContactCard;

const Buttons = styled.div`
padding-top:0.6em;
display:flex;
flex-direction:row;
gap:4px;
`
const StyledButton = styled(Button)`
  display: flex;
  border-radius: 8px;
  height:30px;
  padding: 0.1em 3.8em;
`;


const PendingButton = styled(Button)`
display: flex;
border-radius: 8px;
background:none;
color:black;
border: 1px solid;
height:30px;
padding: 0.1em 3.8em;

`


const Availability = styled.div``;

const AvailText = styled.div`
  font-size: 11px;
  padding-top: 0.8em;
`;

const AvailCard = styled.span`
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  height: 210px;
  border-radius: 10px;
  padding: 1em;
`;

const DefCard = styled.span`
display: flex;
flex-direction: column;
background-color: #f5f5f5;
height: 140px;
border-radius: 10px;
padding: 1em;
`;

const Profile = styled.div`
  display: flex;
  flex-direction: row;
  gap: 1em;
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

const Name = styled.div`
  font-weight: 700;
`;

const HighPriorityButton = styled.span`
  background-color: #ffd4e2;
  color: #791931;
  font-size: 12px;
  padding: 3px 1.3em;
  border-radius: 2em;
  cursor: default;
`;

const MediumPriorityButton = styled.span`
  background-color: #fff0ca;
  color: #794119;
  font-size: 12px;
  padding: 3px 1.3em;
  border-radius: 2em;
  cursor: default;
`;

const LowPriorityButton = styled.span`
  background-color: #e3ffa7;
  color: #185f06;
  font-size: 12px;
  padding: 3px 1.3em;
  border-radius: 2em;
  cursor: default;
`;

const Text = styled.div`
  margin-top: 10px;
  display: flex;
  gap: 0.3em;
  flex-direction: column;
`;
