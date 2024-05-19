import React, { useState } from 'react';
import styled, { keyframes, css } from 'styled-components';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { Button } from '@radix-ui/themes';

const initialItems = [
  { id: '1', name: 'Evan Yan', priority: 1, date: 'Monday, 2:00pm-5:00pm, May 21th', lastHangout: '1d ago' },
  { id: '2', name: 'Bobby Flay', priority: 2, date: 'Wednesday, 8:00pm-9:00pm, May 23th', lastHangout: '30d ago' },
  { id: '3', name: 'Timothy Lim', priority: 3, date: 'Thursday, 9:00pm-11:00pm, May 24th', lastHangout: '2d ago' },
  { id: '4', name: 'Gordon Ramsay', priority: 1, date: 'Friday, 9:00am-11:00am, May 25th', lastHangout: '12d ago' },
  { id: '5', name: 'Lebron James', priority: 2, date: 'Saturday, 3:00pm-5:00pm, May 26th', lastHangout: '7d ago' },
];

const App = () => {
  const [items, setItems] = useState(initialItems);

  const handleCheckboxClick = (id) => {
    setItems((prevItems) =>
      prevItems.map(item => item.id === id ? { ...item, removing: true } : item)
    );
    setTimeout(() => {
      setItems((prevItems) => prevItems.filter(item => item.id !== id));
    }, 1000); // 1 second delay before removal
  };

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

  const handleDragEnd = (result) => {
    if (!result.destination) return;

    const newItems = Array.from(items);
    const [reorderedItem] = newItems.splice(result.source.index, 1);
    newItems.splice(result.destination.index, 0, reorderedItem);

    setItems(newItems);
  };

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <Droppable droppableId="list">
        {(provided) => (
          <List {...provided.droppableProps} ref={provided.innerRef}>
            {items.map((item, index) => (
              <Draggable key={item.id} draggableId={item.id} index={index}>
                {(provided, snapshot) => (
                  <ListItem
                    ref={provided.innerRef}
                    {...provided.draggableProps}
                    {...provided.dragHandleProps}
                    removing={item.removing}
                    isDragging={snapshot.isDragging}
                  >
                    <input type="checkbox" onChange={() => handleCheckboxClick(item.id)} />
                    <Body>
                      <ItemContent>
                        <SubHead>You and <b>{item.name}</b> should hangout at </SubHead>
                        <Head>{item.date}</Head>
                      </ItemContent>
                      <Tags>
                        {renderPriorityButton(item.priority)}
                        <Hangout>Last Hangout: {item.lastHangout}</Hangout>
                      </Tags>
                    </Body>
                  </ListItem>
                )}
              </Draggable>
            ))}
            {provided.placeholder}
          </List>
        )}
      </Droppable>
    </DragDropContext>
  );
};

const slideOut = keyframes`
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(-20px);
  }
`;

const List = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const ListItem = styled.li`
  background: #F5F5F5;
  margin-bottom: 10px;
  padding: 15px 0px 15px 10px;
  border-radius:10px;
  display:flex;
  flex-direction:row;
  align-items:center;
  gap:15px;

  animation: ${props => props.removing ? css`${slideOut} 0.5s forwards` : 'none'};
  box-shadow: ${props => props.isDragging ? '0 2px 5px rgba(0,0,0,0.2)' : 'none'};
`;

const Body = styled.div`
  display:flex;
  flex-direction:column;
`;

const ItemContent = styled.div`
  display: flex;
  flex-direction:column;
  line-height:16px;
  p {
    margin: 0;
  }
`;

const SubHead = styled.div`
  font-size:12px;
`;

const Head = styled.div`
  font-weight:700;
  font-size:14px;
`;

const Tags = styled.div`
  padding-top:10px;
  display:flex;
  flex-direction:row;
  justify-content:space-between;
  align-items:center;
`;

const HighPriorityButton = styled.span`
  background-color:#FFD4E2;
  color: #791931;
  font-size:12px;
  padding:3px 1.3em;
  border-radius:2em;
  cursor:default;
`;

const MediumPriorityButton = styled.span`
  background-color:#FFF0CA;
  color: #794119;
  font-size:12px;
  padding:3px 1.3em;
  border-radius:2em;
  cursor:default;
`;

const LowPriorityButton = styled.span`
  background-color:#E3FFA7;
  color: #185F06;
  font-size:12px;
  padding:3px 1.3em;
  border-radius:2em;
  cursor:default;
`;

const Hangout = styled.div`
  color: #858585;
  font-size:12px;
`;

export default App;