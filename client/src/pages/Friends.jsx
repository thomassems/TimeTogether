import styled from "styled-components";
import ContactCard from "../components/ContactCard";

const contacts = [{
    name:'Evan Yan',
    priority: 1,
    lastHangout: '204920',
    isAvailable: true,
    event: {
        date:'Thursday, 8:00pm-9:00pm, May 20th'
    },
    
},{
    name:'Evan Yan',
    priority: 2,
    lastHangout: '204920',
    isAvailable: true,
    event: {
        date:'Thursday, 8:00pm-9:00pm, May 20th'
    },
    
},{
    name:'Evan Yan',
    priority: 3,
    lastHangout: '204920',
    isAvailable: true,
    event: {
        date:'Thursday, 8:00pm-9:00pm, May 20th'
    },
    
},
{
    name:'Average Joe',
    priority: 3,
    lastHangout: '204920',
    isAvailable: false,
    event: {
        date:'Thursday, 8:00pm-9:00pm, May 20th'
    }
}]

function Friends() {
  return (
    <MyFriends>
        <Title>Your Contacts</Title>
        <ContactList>
        {contacts.map(({ name, priority, lastHangout, isAvailable, event }, i) => (
            <ContactCard id={i} name={name} priority={priority} lastHangout={lastHangout} isAvailable={isAvailable} event={event} />
            ))}
        </ContactList>
    </MyFriends>
  )
}

export default Friends

const Title = styled.div`
  font-weight: 700;
  font-size: 18px;
  margin-bottom:3px;
`;

const MyFriends = styled.div`
    padding-top:1em;
`

const ContactList = styled.div`
    display:flex;
    flex-direction:column;
    gap:0.8em;
`
