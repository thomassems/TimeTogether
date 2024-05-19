import styled from "styled-components"
import Pending from '../graphics/pending.png'
import Confirmed from '../graphics/confirmed.svg'
function EventCard({day, time, date, name, status}) {
  return (
    <Card>
        <div>
        <Header>{day}</Header>
        <Header>{time}</Header>
        <SubHead>{date}</SubHead>
        </div>
        <Footer>
            {status ?
            <>
            <IconConfirm src={Confirmed}/>
            <Scheduled>Scheduled with {name}</Scheduled>
            </> 
            :
            <>
            <Icon src={Pending}/>
            <Scheduled>Waiting on {name}</Scheduled>
            </>

            }
            
        </Footer>

    </Card>
  )
}

export default EventCard

const Card = styled.div`
    line-height:16px;
    background-color:#F5F5F5;
    width:140px;
    height:140px;
    padding:0.5em;
    border-radius:10px;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
`

const Header = styled.div`
    font-weight:700;
    font-size:13px;

`

const SubHead = styled.div`
    font-weight:700;
    font-size:13px;
    color: #858585;
`

const Footer = styled.div`
    display:flex;
    justify-content: space-between;
    align-items:center;
`

const Icon = styled.img`
    width:22px;
    height:22px;
`

const Scheduled = styled.div`
    padding-left:1em;
    text-align:right;
    font-size:13px;
`

const IconConfirm = styled.img`
width:18px;
height:18px;
`