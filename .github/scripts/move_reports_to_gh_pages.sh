#!/usr/bin/env bash

# Get reference to project root directory
PROJECT_ROOT=$(dirname "$(dirname "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)")")

# Remove existing directory, /tmp/cryptomath-book, and all its contents (if it exists)
if [ -d "/tmp/cryptomath-book" ]; then
  rm -rf /tmp/cryptomath-book
fi

# Clone the gh-page branch for repo with our pages source into a new directory under /tmp
git clone --branch gh-pages --single-branch https://x-access-token:${GITHUB_TOKEN}@github.com/dandoug/cryptomath-book.git /tmp/cryptomath-book

# Delete everything except .git directory
find /tmp/cryptomath-book -mindepth 1 ! -path '/tmp/cryptomath-book/.git' ! -path '/tmp/cryptomath-book/.git/*' -exec rm -rf {} +

# Move the built html contents to the root of cryptomath-book
cp -R "${PROJECT_ROOT}/_build/html/." /tmp/cryptomath-book/

# Move the report files to /tmp/cryptomath-book/reports
mkdir -p /tmp/cryptomath-book/cireports
REPORTS_TO_MOVE=("coverage.xml")
for REPORT in "${REPORTS_TO_MOVE[@]}"; do
  mv "$PROJECT_ROOT/$REPORT" /tmp/cryptomath-book/cireports/
done

# Mark the directory as not being jekyll
touch /tmp/cryptomath-book/.nojekyll

# Stage and commit all the modified or added files in the /tmp/cryptomath-book directory
(
  cd /tmp/cryptomath-book && \
  git config user.name "github-actions[bot]" && \
  git config user.email "github-actions[bot]@users.noreply.github.com" && \
  git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/dandoug/cryptomath-book.git && \
  git add . && \
  git commit --amend --no-edit && \
  git push --force origin gh-pages
)
  
# cleanup the /tmp/cryptomath-book directory
rm -rf /tmp/cryptomath-book
