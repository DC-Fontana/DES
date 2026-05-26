import { ScreenGrid } from '../components/screen-grid';

export default function HomePage() {
  return (
    <main className="des-shell">
      <section className="des-hero">
        <h1>DES Operating System</h1>
        <p>
          Voice-first assistant for planning, building, and operating projects with private memory
          and approval-based computer control.
        </p>
      </section>
      <ScreenGrid />
    </main>
  );
}
