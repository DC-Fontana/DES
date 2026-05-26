'use client';

import { motion } from 'framer-motion';

const cards = [
  'Voice Interface',
  'Memory Center',
  'Projects',
  'System Activity'
];

export function MotionValuePanel() {
  return (
    <section className="des-grid">
      {cards.map((card, index) => (
        <motion.article
          className="des-card"
          key={card}
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.08, duration: 0.35 }}
        >
          {card}
        </motion.article>
      ))}
    </section>
  );
}
