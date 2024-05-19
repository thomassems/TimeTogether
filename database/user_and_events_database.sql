--
-- PostgreSQL database dump
--

-- Dumped from database version 14.12 (Homebrew)
-- Dumped by pg_dump version 16.1

-- Started on 2024-05-18 14:33:54 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: thomassems
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO thomassems;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 209 (class 1259 OID 16385)
-- Name: User; Type: TABLE; Schema: public; Owner: thomassems
--

CREATE TABLE public."User" (
    friend integer,
    username character varying(20),
    "uID" integer,
    priority integer,
    "lastTalkedTo" timestamp without time zone
);


ALTER TABLE public."User" OWNER TO thomassems;

--
-- TOC entry 212 (class 1259 OID 16410)
-- Name: event_participants; Type: TABLE; Schema: public; Owner: thomassems
--

CREATE TABLE public.event_participants (
    "eID" integer,
    "uID" integer
);


ALTER TABLE public.event_participants OWNER TO thomassems;

--
-- TOC entry 210 (class 1259 OID 16390)
-- Name: events; Type: TABLE; Schema: public; Owner: thomassems
--

CREATE TABLE public.events (
    "eID" integer NOT NULL,
    "eventName" character varying(100) NOT NULL,
    "eventDescription" character varying(250) NOT NULL,
    "eventLocation" character varying(100),
    "eventTime" timestamp without time zone
);


ALTER TABLE public.events OWNER TO thomassems;

--
-- TOC entry 211 (class 1259 OID 16400)
-- Name: invites; Type: TABLE; Schema: public; Owner: thomassems
--

CREATE TABLE public.invites (
    "uID" integer,
    "friendID" integer,
    "eID" integer
);


ALTER TABLE public.invites OWNER TO thomassems;

--
-- TOC entry 3652 (class 0 OID 16385)
-- Dependencies: 209
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: thomassems
--

COPY public."User" (friend, username, "uID", priority, "lastTalkedTo") FROM stdin;
\N	Bob	\N	\N	\N
\N	Nick	2	0	\N
\N	Nick	2	0	\N
2	Mike	3	3	\N
3	Nick	2	1	\N
\.


--
-- TOC entry 3655 (class 0 OID 16410)
-- Dependencies: 212
-- Data for Name: event_participants; Type: TABLE DATA; Schema: public; Owner: thomassems
--

COPY public.event_participants ("eID", "uID") FROM stdin;
\.


--
-- TOC entry 3653 (class 0 OID 16390)
-- Dependencies: 210
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: thomassems
--

COPY public.events ("eID", "eventName", "eventDescription", "eventLocation", "eventTime") FROM stdin;
1	Nick's soccer tourny	Watch Nick get hat trick	Etobicoke	2024-05-18 12:01:35.53536
2	Hackathon	Start coding	Milton	2024-05-18 13:02:09.647184
\.


--
-- TOC entry 3654 (class 0 OID 16400)
-- Dependencies: 211
-- Data for Name: invites; Type: TABLE DATA; Schema: public; Owner: thomassems
--

COPY public.invites ("uID", "friendID", "eID") FROM stdin;
3	2	1
3	2	2
\.


--
-- TOC entry 3510 (class 2606 OID 16404)
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: thomassems
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY ("eID");


--
-- TOC entry 3511 (class 2606 OID 16405)
-- Name: invites fk; Type: FK CONSTRAINT; Schema: public; Owner: thomassems
--

ALTER TABLE ONLY public.invites
    ADD CONSTRAINT fk FOREIGN KEY ("eID") REFERENCES public.events("eID");


--
-- TOC entry 3512 (class 2606 OID 16413)
-- Name: event_participants fk; Type: FK CONSTRAINT; Schema: public; Owner: thomassems
--

ALTER TABLE ONLY public.event_participants
    ADD CONSTRAINT fk FOREIGN KEY ("eID") REFERENCES public.events("eID");


--
-- TOC entry 3661 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: thomassems
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2024-05-18 14:33:54 EDT

--
-- PostgreSQL database dump complete
--

