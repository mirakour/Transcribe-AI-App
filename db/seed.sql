INSERT INTO transcriptions (filename, source_type, speaker_count)
VALUES 
('team_meeting.mp3', 'live', 3),
('project_briefing.mp4', 'zoom', 2),
('startup_pitch.mp3', 'upload', 2),
('interview_session.mp4', 'youtube', 4),
('webinar_recap.mp3', 'upload', 1),
('daily_standup.wav', 'live', 3),
('research_discussion.mp3', 'zoom', 2),
('client_call.mp4', 'upload', 2),
('panel_talk.mp3', 'youtube', 4),
('sales_training.mp3', 'upload', 3);

INSERT INTO summaries (transcription_id, summary_text)
VALUES 
(1, 'Team discussed Q2 goals and delegated action items.'),
(2, 'Client requirements were outlined with timeline estimations.'),
(3, 'Entrepreneur pitched AI-driven product concept.'),
(4, 'HR and candidate discussed role expectations.'),
(5, 'Solo webinar on productivity habits.'),
(6, 'Daily tasks assigned; blockers discussed.'),
(7, 'Group debated statistical methods for analysis.'),
(8, 'Budget and scope clarified with the client.'),
(9, 'Multiple experts discussed AI trends.'),
(10, 'Training on handling objections in sales calls.');