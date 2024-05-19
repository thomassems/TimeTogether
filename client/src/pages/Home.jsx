import styled from "styled-components";
import { ScrollArea, Text, Flex } from "@radix-ui/themes";
import EventCard from "../components/EventCard";
import Reccomendation from "../components/Recommendation";
const events = [
    {
        day: 'Monday',
        time: '8:00pm-9:00pm',
        date: 'May 20th',
        name: 'Jason',
        status: true,
    },
    {
        day: 'Thursday',
        time: '3:00pm-7:00pm',
        date: 'May 25th',
        name: 'Tom',
        status: false
},{
    day: 'Friday',
    time: '5:00pm-9:00pm',
    date: 'May 29th',
    name: 'Bryan',
    status: false
},

]




function Home() {
  return (
    <Wrapper>
      <Events>
        <Title>Your Events</Title>
        <ScrollArea
          type="always"
          scrollbars="horizontal"
          style={{ height: 160 }}
        >
          <Flex gap="2" p="0" width="400px">
          {events.map(({ day, time, date, name, status }, i) => (
            <EventCard id={i} day={day} time={time} date={date} name={name} status={status} />
            ))}
          </Flex>
        </ScrollArea>
      </Events>
      <Suggest>
      <Title>Recommendations</Title>
      <Sub>Dismiss recommendations as you wish</Sub>
        <Reccomendation/>
      </Suggest>
    </Wrapper>
  );
}

export default Home;

const Wrapper = styled.div``;

const Events = styled.div`
  padding-top: 1em;
  margin-bottom:0.5em;
`;

const Suggest = styled.div``;

const Title = styled.div`
  font-weight: 700;
  font-size: 18px;
  margin-bottom:3px;
`;

const LoEvents = styled.div``;

const Sub = styled.div`
line-height:8px;
margin-bottom:1em;
 color: #5E5E5E;
 font-size:12px;
`