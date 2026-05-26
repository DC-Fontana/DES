import { MotionValuePanel } from '../components/motion-value-panel';

export default function HomePage() {
  return (
    <main className="des-shell">
      <section className="des-hero">
        <h1>DES</h1>
        <p>Voice-first private AI operating system.</p>
      </section>
      <MotionValuePanel />
    </main>
  );
}
