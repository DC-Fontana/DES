'use client';

import { motion } from 'framer-motion';

const screens = [
  'Home',
  'Voice Interface',
  'Memory Center',
  'Projects',
  'Skills',
  'Integrations',
  'Settings',
  'System Activity'
];

export function ScreenGrid() {
  return (
    <section className="des-grid">
      {screens.map((name, i) => (
        <motion.article
          className="des-card"
          key={name}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: i * 0.05, duration: 0.3 }}
        >
          <h3>{name}</h3>
          <p>Phase-1 scaffold for {name.toLowerCase()}.</p>
        </motion.article>
      ))}
    </section>
  );
}
